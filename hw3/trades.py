import csv
import datetime

class OHLC():
    def __init__(self, name, date, time, start=0.0, maxc=0.0, minc=0.0, end=0.0):
        self.name = name
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        dt = date.split()
        self.date = dt[0]+'T'+dt[1]+'Z'
        self.time = time
        self.start = start
        self.end = end
        self.maxc = maxc
        self.minc = minc

daystart = 7.00*3600
dayend = 3.00*3600


def trading(dlit):
    tokens = {}
    interval_top = 7.00*3600+dlit*60
    output_tokens = []
    with open('trades.csv', 'r') as file:
        base = csv.reader(file)
        row = next(base)[3].split()
        row = row[0] + ' 07:00:00'
        interval = datetime.datetime.strptime(row, '%Y-%m-%d %H:%M:%S')
        for row in base:
            rowtimedate = row[3].split()
            rowtime = rowtimedate[1]
            time = float(str(int(rowtime[:2])*3600+int(rowtime[3:5])*60+int(rowtime[6:8]))+rowtime[8:])
            if time < daystart and time > dayend:
                interval_top = 7.00*3600+dlit*60
                interval = datetime.datetime.strptime(rowtimedate[0]+' 7:00:00', '%Y-%m-%d %H:%M:%S')
            else:
                current_row = OHLC(row[0], interval, time, float(row[1]), float(row[1]), float(row[1]))
                if current_row.time < dayend:
                    current_row.time += 24*3600
                if current_row.time <= interval_top:
                    if current_row.name not in tokens.keys():
                        tokens.update({current_row.name:current_row})
                    tokens[current_row.name].end = current_row.start    
                    if current_row.start > tokens[current_row.name].maxc:
                        tokens[current_row.name].maxc = current_row.start
                    if current_row.start < tokens[current_row.name].minc:
                        tokens[current_row.name].minc = current_row.start
                else:
                    if tokens != {}:
                        for i in tokens.keys():
                            output_tokens.append([tokens[i].name, tokens[i].date, tokens[i].start,
                                                tokens[i].maxc, tokens[i].minc, tokens[i].end])
                        name = 'ohlc_' + str(dlit) + 'min.csv'
                        with open(name, 'w') as output:
                            writer = csv.writer(output, delimiter=',')
                            writer.writerows(output_tokens)
                    
                    interval += datetime.timedelta(minutes = dlit)

                    interval_top += dlit*60
                    tokens = {}

trading(5)
trading(30)
trading(240)                
            