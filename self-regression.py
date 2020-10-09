import warnings
warnings.filterwarnings('ignore') # 計算警告を非表示
warnings.simplefilter('ignore')

import pandas as pd
import numpy as np
import statsmodels.api as sm

data = pd.read_csv('/app/data.csv')

print(data)

# date open high low close volume
y = np.array(data["open"].values)

for i in range(2): #0次と1次の和分過程で探索
    delta_y = np.diff(y, n=i)
    resdiff = sm.tsa.arma_order_select_ic(delta_y, ic="aic", trend="nc")
    print(resdiff)