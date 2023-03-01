from closestPair import *
import numpy as np
import pandas as pd
import plotly
import plotly.express as px

def makegraph(points, closestPair) :
    # Mengubah list point dan closestPair menjadi array
    npoints = np.array(points)
    nclosest = np.array(closestPair)

    # Untuk kasus 3D
    if len(nclosest[0]) == 3 :
        # Mengubah array menjadi dataframe
        df = pd.DataFrame({'x':npoints[:,0], 
                           'y':npoints[:,1],
                           'z':npoints[:,2]})
    
        newdf = pd.DataFrame({'x':nclosest[:,0],
                              'y':nclosest[:,1],
                              'z':nclosest[:,2]})
    
        # Memberi attribut Closest TRUE pada point yang menjadi closestPair
        d = pd.merge(df, newdf, on=['x','y','z'], how='left', indicator='Closest')
        d['Closest'] = np.where(d.Closest == 'both', True, False)

        # Visualisasi data
        fig3d = px.scatter_3d(d, x='x', y='y', z='z', color='Closest')
        fig3d.show()

    # Untuk kasus 2D
    elif len(nclosest[0]) == 2 :
        # Mengubah array menjadi dataframe
        df = pd.DataFrame({'x':npoints[:,0], 
                           'y':npoints[:,1]})
    
        newdf = pd.DataFrame({'x':nclosest[:,0],
                              'y':nclosest[:,1]})
    
        # Memberi attribut Closest TRUE pada point yang menjadi closestPair
        d = pd.merge(df, newdf, on=['x','y'], how='left', indicator='Closest')
        d['Closest'] = np.where(d.Closest == 'both', True, False)

         # Visualisasi data
        fig2d = px.scatter(d, x='x', y='y', color='Closest')
        fig2d.show()

    # Untuk kasus N-Dimensi
    else :
        # Mengubah array menjadi dataframe
        trydf = pd.DataFrame()
        for i in range (len(nclosest[0])) :
            trydf[i] = npoints[:,i]

        trynewdf = pd.DataFrame()
        for i in range (len(nclosest[0])) :
            trynewdf[i] = nclosest[:,i]

        # Memberi attribut Closest TRUE pada point yang menjadi closestPair
        tryattribut = list(range(len(nclosest[0])))

        tryd = pd.merge(trydf, trynewdf, on=tryattribut, how='left', indicator='Closest')
        tryd['Closest'] = np.where(tryd.Closest == 'both', True, False)

         # Visualisasi data
        figmatrix = px.scatter_matrix(tryd, color='Closest')
        figmatrix.show()

if __name__ == "__main__":
    points = createPoints(800,2)
    closestPair = closestPointsDividenConquer(points)
    makegraph(points,closestPair)