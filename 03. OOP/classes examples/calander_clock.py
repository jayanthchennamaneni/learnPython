def plot_data(y, X, Y):
        ig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        for i, path_line in enumerate(y):
            for j, conc in enumerate(Y[i]):
                for k, data in enumerate(conc):
                    ax1.plot(X, data, linestyle='-')
                    
        
        
        plt.xlabel("xdata")
        plt.ylabel("ydata")
        plt.legend()
        plt.show()


if time_var.get() and conc_var.get():
    plot_data(y,X, Y)

if time_var.get() and conc_var.get():
    plot(y,X, Y)

if time_var.get() and conc_var.get():
    plot(y,X, Y)

if time_var.get() and conc_var.get():
    plot(y,X, Y)

    


