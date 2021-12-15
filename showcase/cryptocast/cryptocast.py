# import libs
import pandas as pd
import quandl
from datetime import timedelta
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from datetime import datetime
from datetime import timedelta
import warnings

warnings.filterwarnings("ignore")

# main class cryptocast
class cryptocast:

    # method to init
    def __init__(self):

        # add coin info to self
        self.coin = 'btc'
        
        # add slot for data
        self.data = None

    # method to get the data
    def get_data(self):

        # read in api_key
        with open('cryptocast/api_key.txt') as key_file:
            api_key = key_file.read()

        # set quandl config
        quandl.ApiConfig.api_key = api_key

        # get the dataset
        raw_df = quandl.get('BITFINEX/BTCEUR')

        # store data
        self.data = raw_df

    # method to prep data
    def prep_data(self):

        # load data
        prep_df = self.data

        # reset the index
        prep_df.reset_index(inplace = True)

        # select relevant vars
        prep_df = prep_df[['Date', 'High', 'Volume', 'Ask']]

        # declare date format
        prep_df.Date = pd.to_datetime(prep_df.Date)

        # sort data by date
        prep_df.sort_values(by = ["Date"], ascending = True, inplace = True)

        # get the last date
        last_day = prep_df.Date[prep_df.shape[0] - 1]

        # get tomorrow
        new_day = last_day + timedelta(days = 1)

        # open new dataframe
        forecast_df = pd.DataFrame(index = [0], columns = ["Date"])

        # fill it with nw date
        forecast_df.Date[0] = new_day

        # append dataframe
        prep_df = prep_df.append(forecast_df, ignore_index = True)

        # find numeric variables
        num_vars = list(prep_df.select_dtypes(include = np.number))

        # loop over lags
        for i in [1, 2, 7]:
            for j in num_vars:
                prep_df[[str("lag_") + str(i) + str("_") + str(j)]] = prep_df[[j]].shift(i)

        # change names to lower
        prep_df.columns = [x.lower() for x in prep_df.columns]

        # drop NaNs in the beginning of the data
        prep_df = prep_df.iloc[-200:]

        # reset index again
        prep_df.reset_index(inplace = True)

        # store the prepped data
        self.data = prep_df

    # method to forecast
    def forecast(self):

        # build the relevant df
        df = self.data[["date", "high"] + list(self.data.filter(regex = "lag_*"))]

        # declare format
        df.date = pd.to_datetime(df.date)

        # define the train period
        next_day_index = df.shape[0] - 1

        # train index
        train_index = df.index[df.date == df.date[df.shape[0] - 2] - timedelta(weeks = 4)].tolist()[0]

        # open evaluation container
        eval_df = pd.DataFrame({"date": df.date[(train_index + 1):],
                            "high": df.high[(train_index + 1):],
                            "pred": np.nan})

        # unselect the date
        df.drop(["date"], axis = 1, inplace = True)

        # loop over data set
        for i in range(train_index, (df.shape[0]-1)):

            # build x_train
            x_train = df[:i].drop(["high"], axis = 1, inplace = False)

            # build y_train
            y_train = df.high[:i]

            # build x_test
            x_test = df.drop(["high"], axis = 1, inplace = False).loc[[(i+1)]]

            # define model parameters
            mod = GradientBoostingRegressor(n_estimators = 100)
            mod.fit(x_train, y_train)
            eval_df.at[(i+1), "pred"] = mod.predict(x_test)[0]

        # compute MAPE
        MAPE = (abs(eval_df.high - eval_df.pred)/eval_df.high).dropna().mean()

        # store output
        self.MAPE = MAPE
        self.message = str("Tomorrow I expect the bitcoin price to be: ") + str(round(eval_df.iloc[[eval_df.shape[0]-1]].pred.tolist()[0])) + str(" Us-Dollars! I was trained with a MAPE of: ") + str(round(MAPE, 4))
