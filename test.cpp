// =====================================================================================
//
//       Filename:  test.cpp
//
//        Version:  1.0
//        Created:  Wednesday 17 June 2020 01:14:21  IST
//       Revision:  none
//       Compiler:  g++
//
// =====================================================================================

#include<iostream>
#include<stdlib.h>

using namespace std;

template<class T>
class Queue{
    private:
        int front,rear;
        T *queue;
        int maxsize;
    public:
        Queue(int maxqueuesize){
                front=0;
                rear=-1;
                maxsize=maxqueuesize;
                queue=new T[maxsize];
        }
        int isempty();
        int isfull();
        void insert();
        void deletion();
        void display();
};

template<class T>
int Queue<T>::isempty(){
    if(front==0&&rear==-1||front==rear)
        return 1;
    else
        return 0;
}

template<class T>
int Queue<T>::isfull(){
    if(rear==maxsize-1)
        return 1;
    else
        return 0;
}


template<class T>
void Queue<T>::insert(){
     T ele;
     if(isfull())
     cout<<"\nSorry the queue is full!";
     else
     {
     cout<<"\nEnter the element to insert : ";
     cin>>ele;
     queue[++rear]=ele;
     }
}

template<class T>
void Queue<T>::deletion(){
     if(isempty())
     cout<<"\nSorry the queue is empty!";
     else
     cout<<"\nDeleted element of the queue is : "<<queue[front++];
}

template<class T>
void Queue<T>::display(){
     if(isempty())
     cout<<"\nSorry the queue is empty!";
     else
     {
         cout<<"\nQueue elements are : ";
         for(int i=front;i<=rear;i++)
         {
                 cout<<"\t"<<queue[i];
         }
     }
     cout<<endl;
}

int main(){
    int ch;
    Queue<int> q(20);
    cout<<"\n 1.Insertion \n 2.Deletion \n 3.Display Queue \n 4.Exit \n";
    do{
        cout<<"Enter your Choice:";
        cin>>ch;
        switch(ch){
            case 1:
                q.insert();
                break;
            case 2:
                q.deletion();
                break;
            case 3:
                q.display();
                break;
            case 4:
                exit(0);
                break;
            default: cout<<"\nWrong Choice Entered!";

            }
    }while(ch<=4);
    return 0;
}

