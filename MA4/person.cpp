#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		long fib(int);
	private:
		int age;
		long calculateFibonacci(int);  // Private Fibonacci calculation method
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}

long Person::calculateFibonacci(int n){
	if (n <= 1)
	 	return n;
    else
    	return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
}

long Person::fib() {
    return calculateFibonacci(age);
}

extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	long Person_fib(Person * person, int n) {return person->fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}