"""THAILAND AIR TRAFFIC STATISTIC ANALYSIS"""
def all_data():
    """Return list from fetch data csv"""

    import csv
    import pygal as pg
    main_data = csv.reader(open('airtrafficstats.csv', newline=''))
    main_data = [row for row in main_data]

    cnx = []
    for i in main_data:
        if i[0] == "CNX":
            cnx.append(i)

    flight_ = []
    for i in cnx:
        if i[1] == "Flight":
            flight_.append(i)

    arrive_2015 = []
    depar_2015 = []
    for i in flight_:
        if i[3] == "2015":
            arrive_2015.append(int(i[5]))
            depar_2015.append(int(i[6]))

    graph = pg.Line(x_labels_major_count=12, show_minor_x_labels=True, truncate_legend=40, \
    legend_at_bottom=False, truncate_label=100)
    graph.title = 'CNX Flight 2015'
    graph.x_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', \
    'September', 'October', 'November', 'December']
    graph.add('Arrive | From', arrive_2015)
    graph.add('Deperture | To', depar_2015)
    graph.range = [150, 300]
    graph.render_to_file('cnx_flight_2015.svg')

    print(arrive_2015)
    print(depar_2015)
all_data()
