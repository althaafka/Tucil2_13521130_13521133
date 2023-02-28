from closestPair import *
import numpy as np
import pandas as pd
import plotly
import plotly.express as px

def makegraph(points, closestPair) :
    npoints = np.array(points)
    nclosest = np.array(closestPair)

    if len(nclosest[0]) == 3 :
        df = pd.DataFrame({'x':npoints[:,0], 
                           'y':npoints[:,1],
                           'z':npoints[:,2]})
    
        newdf = pd.DataFrame({'x':nclosest[:,0],
                              'y':nclosest[:,1],
                              'z':nclosest[:,2]})
    
        d = pd.merge(df, newdf, on=['x','y','z'], how='left', indicator='Closest')
        d['Closest'] = np.where(d.Closest == 'both', True, False)

        fig3d = px.scatter_3d(d, x='x', y='y', z='z', color='Closest')
        fig3d.show()

    elif len(nclosest[0]) == 2 :
        df = pd.DataFrame({'x':npoints[:,0], 
                           'y':npoints[:,1]})
    
        newdf = pd.DataFrame({'x':nclosest[:,0],
                              'y':nclosest[:,1]})
    
        d = pd.merge(df, newdf, on=['x','y'], how='left', indicator='Closest')
        d['Closest'] = np.where(d.Closest == 'both', True, False)

        fig2d = px.scatter(d, x='x', y='y', color='Closest')
        fig2d.show()

    else :
        trydf = pd.DataFrame()
        for i in range (len(nclosest[0])) :
            trydf[i] = npoints[:,i]

        trynewdf = pd.DataFrame()
        for i in range (len(nclosest[0])) :
            trynewdf[i] = nclosest[:,i]

        tryattribut = list(range(len(nclosest[0])))

        tryd = pd.merge(trydf, trynewdf, on=tryattribut, how='left', indicator='Closest')
        tryd['Closest'] = np.where(tryd.Closest == 'both', True, False)

        figmatrix = px.scatter_matrix(tryd, color='Closest')
        figmatrix.show()

if __name__ == "__main__":
    points = createPoints(40,2)
    closestPair = closestPointsDividenConquer(points)
    makegraph(points,closestPair)