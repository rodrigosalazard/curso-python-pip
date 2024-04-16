import matplotlib.pyplot as plot


def generate_pie_chart():
    labels = ["A","B","C"]
    values = [23,75,26]
    
    fig,ax = plot.subplots()
    ax.pie(values, labels = labels)
    # plot.show()
    plot.savefig("pie.png")
    plot.close()
    
    
