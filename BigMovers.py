//@version=5

indicator("Percent Change Monitor", overlay=false)

currentTimeFrame = input.timeframe("","Timeframe")

stock1 = input.symbol(defval="AAPL", title="Symbol 1")

stock2 = input.symbol(defval="MSFT", title="Symbol 2")

stock3 = input.symbol(defval="AMZN", title="Symbol 3")

stock4 = input.symbol(defval="TSLA", title="Symbol 4")

stock5 = input.symbol(defval="GOOGL", title="Symbol 5")

Price1 = request.security(stock1, currentTimeFrame, close[1])

Price2 = request.security(stock1, currentTimeFrame, close)

Price3 = request.security(stock2, currentTimeFrame, close[1])

Price4 = request.security(stock2, currentTimeFrame, close)

Price5 = request.security(stock3, currentTimeFrame, close[1])

Price6 = request.security(stock3, currentTimeFrame, close)

Price7 = request.security(stock4, currentTimeFrame, close[1])

Price8 = request.security(stock4, currentTimeFrame, close)

Price9 = request.security(stock5, currentTimeFrame, close[1])

Price10 = request.security(stock5, currentTimeFrame, close)

PercentChg3 = ((Price2 - Price1)+ (Price4 - Price3)+ (Price6 - Price5)+ (Price8 - Price7)+ (Price10 - Price9))/(Price1+Price3+Price5+Price7+Price9) *100

plot(PercentChg3,style=plot.style_columns,color=PercentChg3>0 ? color.green : color.red )