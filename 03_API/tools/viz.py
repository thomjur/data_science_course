import graphviz

def gv_api_general():
    '''
    Simple graph to visualize a simple apie
    '''
    ps = graphviz.Digraph('api-general')
    
    # nodes
    ps.attr('node', shape='Mrecord')

    ps.node('A', 'Program A')
    ps.node('B', '<f0> API|<f1> Program B')
    
    # edges
    ps.edge('A', 'B:f0', label="call")
    ps.edge('B:f0', 'A', label="service")

    # attributes for rendering graph
    ps.graph_attr['rankdir'] = 'LR'  
   
    return ps

def gv_api_web():
    '''
    Simple graph to visualize a simple web api
    '''
    ps = graphviz.Digraph('api-web')
    
    # nodes
    ps.attr('node', shape='ellipse')

    ps.node('A', 'Client')
    ps.node('B', 'Web Server / API')
    ps.node('C', 'Backend Server')

    ps.attr('node', shape='cylinder')
    ps.node('D', 'DB')
    
    # edges
    ps.edge('A', 'B', label="request (http)")
    ps.edge('B', 'A', label="response (JSON/XML)")
    ps.edge('B', 'C', label="calls")
    ps.edge('B', 'D', label="calls")

    # attributes for rendering graph
    ps.graph_attr['rankdir'] = 'LR'  
   
    return ps