
# Assignment1: Find the count of each order status

def countOrderStatus(status):

    status = ['CLOSED', 'PENDING_PAYMENT', 'COMPLETE', 'CLOSED', 'COMPLETE',
            'COMPLETE', 'COMPLETE', 'PROCESSING', 'PENDING_PAYMENT', 'PENDING_PAYMENT']
    
    uniqueStatus = set(status)

    status_count = [(item, status.count(item)) for item in uniqueStatus]
    print(status_count)

# countOrderStatus(['CLOSED', 'PENDING_PAYMENT', 'COMPLETE', 'CLOSED', 'COMPLETE','COMPLETE', 'COMPLETE', 'PROCESSING', 'PENDING_PAYMENT', 'PENDING_PAYMENT'])   

##########################
# Note In the above case insertion order is NOT preserved.
# If Insertion prder to be preserved use below code

def countOrderStatusWithInsertionOrderPreserved(status):
    seen = set()
    unique_words = []
    for word in status:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    print(unique_words)

countOrderStatusWithInsertionOrderPreserved(['CLOSED', 'PENDING_PAYMENT', 'COMPLETE', 'CLOSED', 'COMPLETE','COMPLETE', 'COMPLETE', 'PROCESSING', 'PENDING_PAYMENT', 'PENDING_PAYMENT'])

###################################################################################################### 
# Assignment2: 

def countOrderStatusInTransactions():

    transactions = [[1, 100, 'success'],
    [2, 200, 'pending'],
    [3, 150, 'success'],
    [4, 300, 'failed'],
    [5, 400, 'success'],
    [6, 250, 'pending'],
    [7, 350, 'failed'],
    [8, 450, 'success'],
    [9, 500, 'pending'],
    [10, 600, 'failed']]

    allStatus = [txn[2] for txn in transactions]
    uniqueStatus = set(allStatus)

    statusWithCount = [(status, allStatus.count(status)) for status in uniqueStatus]
    print(statusWithCount)

# countOrderStatusInTransactions()

###################################################################################################### 
# Assignment3: Find the average salary in each department




