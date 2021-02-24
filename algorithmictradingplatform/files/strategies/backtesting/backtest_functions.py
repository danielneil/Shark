def PrintHtmlREPORT(ticker, strat, retAnalyzer, sharpeRatioAnalyzer, drawDownAnalyzer, tradesAnalyzer):

  with open("/shark/backtest/" + ticker + ".html", 'w') as htmlFile:

        htmlFile.write("<html>")
        htmlFile.write("<head>")
        htmlFile.write("</head>")
        htmlFile.write("<body>")
        htmlFile.write("<h1>Strategy Performance - "+ticker+"</h1>") 
        htmlFile.write("<a href = '/shark/backtest/" + ticker + ".trade.log'>Trade Log</a>")
        htmlFile.write("<br />")
        htmlFile.write("<br />")
        htmlFile.write("<table border=1 style='width: 800px'>")
        htmlFile.write("<tr><th style='background-color: #E0E0E0' colspan='2'>Portfolio Summary</th></tr>") 
        htmlFile.write("<tr><td>Final portfolio value:</td><td>$%.2f</td></tr>" % strat.getResult())
        htmlFile.write("<tr><td>Cumulative returns:</td><td>%.2f %%</td></tr>" % (retAnalyzer.getCumulativeReturns()[-1] * 100))

        sharpeRatio = sharpeRatioAnalyzer.getSharpeRatio(0.05)

        htmlFile.write("<tr><td>Sharpe ratio:</td><td>%.2f</td></tr>" % (sharpeRatio))
        htmlFile.write("<tr><td>Max. drawdown:</td><td>%.2f %%</td></tr>" % (drawDownAnalyzer.getMaxDrawDown() * 100))
        htmlFile.write("<tr><td>Longest drawdown duration:</td><td>%s</td></tr>" % (drawDownAnalyzer.getLongestDrawDownDuration()))
        htmlFile.write("<tr><td style='background-color: #E8E8E8'>Total trades:</td><td>%d</td></tr>" % (tradesAnalyzer.getCount()))
        htmlFile.write("<tr><td style='text-align: right'>Wins:</td><td>%d</td></tr>" % (tradesAnalyzer.getProfitableCount()))
        htmlFile.write("<tr><td style='text-align: right'>Losses:</td><td>%d</td></tr>" % (tradesAnalyzer.getUnprofitableCount()))
        htmlFile.write("</table>")
        htmlFile.write("<br />")

        htmlFile.write("<img src = '/shark/backtest/" + ticker + ".png' />")

        if tradesAnalyzer.getCount() > 0:

            profits = tradesAnalyzer.getAll()

            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Wins + Losses</th></tr>") 
            
            htmlFile.write("<tr><td>Avg. profit:</td><td>$%2.f</td></tr>" % (profits.mean()))
            htmlFile.write("<tr><td>Profits std. dev.:</td><td>$%2.f</td></tr>" % (profits.std()))
            htmlFile.write("<tr><td>Max. profit:</td><td>$%2.f</td></tr>" % (profits.max()))
            htmlFile.write("<tr><td>Min. profit:</td><td>$%2.f</td></tr>" % (profits.min()))

            returns = tradesAnalyzer.getAllReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100)) 
            
            htmlFile.write("</table>")
            htmlFile.write("<br />")

        if tradesAnalyzer.getProfitableCount() > 0:

            profits = tradesAnalyzer.getProfits()

            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Wins</th></tr>") 
            
            htmlFile.write("<tr><td>Avg. profit:</td><td>$%2.f</td></tr>" % (profits.mean()))
            htmlFile.write("<tr><td>Profits std. dev.:</td><td>$%2.f</td></tr>" % (profits.std()))
            htmlFile.write("<tr><td>Max. profit:</td><td>$%2.f</td></tr>" % (profits.max()))
            htmlFile.write("<tr><td>Min. profit:</td><td>$%2.f</td></tr>" % (profits.min()))

            returns = tradesAnalyzer.getPositiveReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100))

            
            htmlFile.write("</table>")
            htmlFile.write("<br />")

        if tradesAnalyzer.getUnprofitableCount() > 0:

            losses = tradesAnalyzer.getLosses()
            
            htmlFile.write("<table border=1 style='width: 800px'>")
            htmlFile.write("<tr><th colspan='2' style='background-color: #E0E0E0'>Losses</th></tr>") 

            htmlFile.write("<tr><td>Avg. loss:</td><td>$%2.f</td></tr>" % (losses.mean()))
            htmlFile.write("<tr><td>Losses std. dev.:</td><td>$%2.f</td></tr>" % (losses.std()))
            htmlFile.write("<tr><td>Max. loss:</td><td>$%2.f</td></tr>" % (losses.min()))
            htmlFile.write("<tr><td>Min. loss:</td><td>$%2.f</td></tr>" % (losses.max()))

            returns = tradesAnalyzer.getNegativeReturns()

            htmlFile.write("<tr><td>Avg. return:</td><td>%2.f %%</td></tr>" % (returns.mean() * 100))
            htmlFile.write("<tr><td>Returns std. dev.:</td><td>%2.f %%</td></tr>" % (returns.std() * 100))
            htmlFile.write("<tr><td>Max. return:</td><td>%2.f %%</td></tr>" % (returns.max() * 100))
            htmlFile.write("<tr><td>Min. return:</td><td>%2.f %%</td></tr>" % (returns.min() * 100))
    
            htmlFile.write("</table>")
            htmlFile.write("<br />")
