// ATD LAB ASSIGNMENT-3
// NAME-ABHISHEK TIBREWAL
// ID-2016UCP1103


#include<bits/stdc++.h>
using namespace std;


class Graph               //Class for Graph and its Adjacency List representation
{
    int V;                                              
    list<int> *adj;                                      
    bool isCyclicUtil(int v, bool visited[], bool *rs);  
    void topologicalSortUtil(int v, bool visited[], stack<int> &Stack);
public:
    Graph(int V);
    void addEdge(int v, int w);   
    bool isCyclic();            
    void topologicalSort(map<int,string>&);
};

Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w); 

}

bool Graph::isCyclicUtil(int v, bool visited[], bool *recStack)
{
    if(visited[v] == false)
    {
        visited[v] = true;
        recStack[v] = true;
        list<int>::iterator i;
        for(i = adj[v].begin(); i != adj[v].end(); ++i)
        {
            if ( !visited[*i] && isCyclicUtil(*i, visited, recStack) )
                return true;
            else if (recStack[*i])
                return true;
        }

    }
    recStack[v] = false; 
    return false;
}

//Function to detect cycle
bool Graph::isCyclic()
{
    bool *visited = new bool[V];
    bool *recStack = new bool[V];
    for(int i = 0; i < V; i++)
    {
        visited[i] = false;
        recStack[i] = false;
    }
    for(int i = 0; i < V; i++)
        if (isCyclicUtil(i, visited, recStack))
            return true;

    return false;
}

void Graph::topologicalSortUtil(int v, bool visited[],stack<int> &Stack)
{
    visited[v] = true;
    list<int>::iterator i;
    for (i = adj[v].begin(); i != adj[v].end(); ++i)
        if (!visited[*i])
            topologicalSortUtil(*i, visited, Stack);
    Stack.push(v);
}

//Topological sorting will give the Serializability order
void Graph::topologicalSort(map<int,string>& m)
{
    stack<int> Stack;
    bool *visited = new bool[V];
    for (int i = 0; i < V; i++)
        visited[i] = false;
    for (int i = 0; i < V; i++)
      if (visited[i] == false)
        topologicalSortUtil(i, visited, Stack);
    while (Stack.empty() == false)
    {
        cout << m[Stack.top()] << " ";
        Stack.pop();
    }
}


int main()
{
	ifstream file("Input-File1.txt");

	//Storing all Transactions
	string T;
	getline(file, T);         			//read first line (TRANS:T1,T2,T3.......)
	vector<string> temp;
	vector<string> trans;
	map<string,int> trans_map;
	map<int,string> trans_map1;
	size_t current, previous = 0;
    current = T.find(":");                                     //split by ':'
    while (current != std::string::npos)
	{
        temp.push_back(T.substr(previous, current - previous));
        previous = current + 1;
        current = T.find(":", previous);
    }
    temp.push_back(T.substr(previous, current - previous));
	current, previous = 0;
    current = temp[1].find(",");                                     //split by ','
    while (current != std::string::npos)
	{
        trans.push_back(temp[1].substr(previous, current - previous));
        previous = current + 1;
        current = temp[1].find(",", previous);
    }
    trans.push_back(temp[1].substr(previous, current - previous));
    cout<<"Transactions are : \n";
	for(int i=0;i<trans.size();i++)
	{
		trans_map[trans[i]]=i;
		trans_map1[i]=trans[i];
		//cout<<trans[i]<<" ";
	}
	map<string,int>::iterator it;
	for(it=trans_map.begin();it!=trans_map.end();it++)
	{
		cout<<it->first<<" "<<it->second<<endl;
	}
	//Storing all Data

	string D;
	getline(file, D);       			//read second line (DATA:A,B,C............)
	vector<string> d;
	vector<string> data;
	current, previous = 0;
    current = D.find(":");                                     //split by ':'
    while (current != std::string::npos)
	{
        d.push_back(D.substr(previous, current - previous));
        previous = current + 1;
        current = D.find(":", previous);
    }
    d.push_back(D.substr(previous, current - previous));
	current, previous = 0;
    current = d[1].find(",");                                     //split by ','
    while (current != std::string::npos)
	{
        data.push_back(d[1].substr(previous, current - previous));
        previous = current + 1;
        current = d[1].find(",", previous);
    }
    data.push_back(d[1].substr(previous, current - previous));
    cout<<endl<<"Data items are : ";
	for(int i=0;i<data.size();i++)
	{
		cout<<data[i]<<" ";
	}
	cout<<endl;
	// Reading  schedule....
  	string str;
  	vector<string> S;
  	map<int,vector<string> > m;
  	while (getline(file, str))
	{
		S.push_back(str);
  	}
  	for(int i=1;i<S.size();i++)
  	{
  		vector<string> temp1;
  		current, previous = 0;
	    current = S[i].find(":");                                     //split by ':'       T1:R(A);
	    while (current != std::string::npos)
		{
	        temp1.push_back(S[i].substr(previous, current - previous));
	        previous = current + 1;
	        current = S[i].find(":", previous);
	    }
	    temp1.push_back(S[i].substr(previous, current - previous));
	    m[i]=temp1;
	}
	map<int,vector<string> >::iterator itr1;
	cout<<endl<<"Operations are:"<<endl;
	for(itr1=m.begin();itr1!=m.end();itr1++)
	{
		cout<<itr1->first<<"	"<<itr1->second[0]<<" "<<itr1->second[1]<<endl;
		//cout<<itr->second[1].substr(2,itr->second[1].find(')') - itr->second[1].find('(') - 1)<<endl;
	}
	//cout<<trans.size()<<endl;
	int arr[trans.size()][trans.size()];
	memset(arr,0,sizeof(arr));
	Graph S_graph(trans.size());
	cout<<endl<<"Conflicting Operations are:"<<endl;
	for(int i=1;i<=m.size();i++)
	{
		for(int j=i+1;j<=m.size();j++)
		{
			// Ti != Tj  and Data(i) == Data(j)
			//cout<<i<<"	"<<j<<" "<<m[i][0]<<" "<<m[j][0]<<" "<<m[i][1].substr(2,m[i][1].find(')') - m[i][1].find('(') - 1)<<" " <<m[j][1].substr(2,m[j][1].find(')') - m[j][1].find('(') - 1)<<endl;
			if(m[i][0] != m[j][0] && m[i][1].substr(2,m[i][1].find(')') - m[i][1].find('(') - 1) == m[j][1].substr(2,m[j][1].find(')') - m[j][1].find('(') - 1))
			{
				// Op(i)==W   or  ( Op(i)==R and Op(j)==W )
				if(m[i][1][0]=='W' || (m[i][1][0]=='R' && m[j][1][0]=='W') )
				{
					if(arr[trans_map[m[i][0]]][trans_map[m[j][0]]]==0)
					{
						S_graph.addEdge(trans_map[m[i][0]], trans_map[m[j][0]]);
						//cout<<m[i][0]<<"------------->"<<m[j][0]<<endl;
						arr[trans_map[m[i][0]]][trans_map[m[j][0]]]++;
					}

					cout<<i<<"------------->"<<j<<endl;

				}
			}
		}
	}
	cout<<endl<<"Graph for given schedule is (Adj. List Representation):"<<endl;
	for(int i=0;i<trans.size();i++)
	{
		cout<<trans_map1[i];
		for(int j=0;j<trans.size();j++)
		{
			if(arr[i][j]!=0)
			{
				cout<<"-->"<<trans_map1[j];
			}
		}
		cout<<endl;
	}
	//cout<<S_graph.isCyclic()<<endl;
	if(S_graph.isCyclic())
	{
		//cout<<"inside-1"<<endl;
		cout<<endl<<"Cycle is present in the Graph. So, given schedule is not Conflict Serializable."<<endl;
	}
	else
	{
		//cout<<"inside-2"<<endl;
		cout<<endl<<"Given schedule is Conflict Serializable as no cycle is present in Graph. \nSerializability order is: < ";
		S_graph.topologicalSort(trans_map1);
		cout<<">"<<endl;
	}
	return 0;
}
