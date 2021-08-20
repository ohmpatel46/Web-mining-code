#take number of iterations as input
n=int(input("Enter the number of iterations: "))
#damping factor
d=0.85;
#SJT,TT,Foodys,VB,SMEC (In order)
pagerank=[1,1,1,1,1]
in_degree=[2,1,2,1,4]
out_degree=[2,2,4,1,1]
for i in range(n):
    pagerank[0]=(1-d)+d*(pagerank[2]/out_degree[2]+pagerank[1]/out_degree[1])
    pagerank[1]=(1-d)+d*(pagerank[2]/out_degree[2])
    pagerank[2]=(1-d)+d*(pagerank[0]/out_degree[0]+pagerank[4]/out_degree[4])
    pagerank[3]=(1-d)+d*(pagerank[2]/out_degree[2])
    pagerank[4]=(1-d)+d*(pagerank[2]/out_degree[2]+pagerank[1]/out_degree[1]+pagerank[0]/out_degree[0]+pagerank[3]/out_degree[3])
print("The page rank for the node SJT is: ",pagerank[0])
print("The page rank for the node TT is: ",pagerank[1])
print("The page rank for the node Foodys is: ",pagerank[2])
print("The page rank for the node VB is: ",pagerank[3])
print("The page rank for the node SMEC is: ",pagerank[4])