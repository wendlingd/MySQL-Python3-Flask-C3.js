from sqlalchemy import create_engine
import pandas as pd


dbconn = create_engine('mysql+mysqlconnector://loginName:PwdIfAny@localhost/bartest')


# ===============================
#   Home page
# ===============================     

'''
In the real app, this query pulls from a summary table - the user has 
already clicked on a specific GroupCode. Contrived example. Your test 
URL needs to be http://localhost:5000/chartUsage/102
'''

def getMicrositeData(GroupCode):
    query = """
        SELECT DISTINCT GroupCode
        FROM groupedbar
        WHERE GroupCode = {}
    """.format(GroupCode)
    
    MicrositeData = pd.read_sql(query, dbconn)
    
    return MicrositeData


# Grouped bar chart of usage
def getChartPVvsSearch(GroupCode):
    query = """
        SELECT ReportMonth, UniquePVsGr, UniqueSearchesGr
        FROM groupedbar
        WHERE GroupCode = {}
        ORDER BY ReportMonth
    """.format(GroupCode)
    
    ChartPVvsSearch = pd.read_sql(query, dbconn)
    
    return ChartPVvsSearch
    

# Table equivalent to the usage chart. Might include extra info, in 
# sortable HTML table.
def getTablePVvsSearch(GroupCode):
    query = """
        SELECT ReportMonth, UniquePVsGr, UniqueSearchesGr
        FROM groupedbar
        WHERE GroupCode = {}
        ORDER BY ReportMonth
    """.format(GroupCode)
    
    TablePVvsSearch = pd.read_sql(query, dbconn)
    
    return TablePVvsSearch
 