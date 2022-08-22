import graphviz

def gv():
    '''
    Simple graph to visualize data science pipeline
    '''
    ps = graphviz.Digraph('ds-pipeline', node_attr={'shape': 'plaintext'})
    
    # nodes
    ps.node('Acquisition')
    ps.node('Cleaning/Transformation')
    ps.node('Analysis')
    ps.node('Visualization/Presentation')
    ps.node('Publication')

    # edges
    ps.edge('Acquisition', 'Cleaning/Transformation')
    ps.edge('Cleaning/Transformation', 'Analysis')
    ps.edge('Analysis', 'Visualization/Presentation')
    ps.edge('Visualization/Presentation', 'Publication')

    # attributes for rendering graph
    ps.graph_attr['rankdir'] = 'LR'  
    ps.edge_attr.update(arrowhead='vee', arrowsize='1')

    return ps