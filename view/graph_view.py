import model.datafilters as df
import matplotlib.pyplot as plt


def getfigure(self): 
         
        labels, values = df.sizeFish()
        fig1, ax1 = plt.subplots(figsize=(10,4.2))
        ax1.pie(values, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=0)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Size of Angler Fish in mm')
        # labels here from example
        # #       ax.plot(x_values, y_values)
        # #       ax.set(xlabel=x_label,
        # #       ylabel=y_label,
        # #       title=title_label)
        #         #plt.show()
        return plt.gcf() 