
def split_my_date(date):
    split_date = date.split(",")

    return split_date[:] + split_date[2]
dates = ["Oct 7, 2009", "Nov 10, 2009", "Jan 10, 2009", "Oct 22, 2009"]


# print(sorted(dates, key=split_my_date, reverse = True))

def dates_and_dict(dates):
    abrv_dates = {
        "Jan": [],
        "Feb": [],
        "Mar": [],
        "Apr": [],
        "May": [],
        "Jun": [],
        "Jul": [],
        "Aug": [],
        "Sep": [],
        "Oct": [],
        "Nov": [],
        "Dec": []
    }

    for date in dates:
        if date[:3] in abrv_dates:
            abrv_dates[date[:3]].append(split_my_date(date))

    # for month in abrv_dates:
    #     if abrv_dates[month] != []:
    #         print(sorted(abrv_dates[month]))
    return abrv_dates

print(dates_and_dict(dates))
