package runner;

import java.sql.SQLException;
import java.util.Scanner;

public class MainRunner {

	public static void main(String[] args)throws SQLException {
		
		boolean exit = false;
		int menu;
		Scanner input = new Scanner(System.in);
		String selection = "\nPlease select the number from the following menu. \n \n" + "Transaction Detail: \n"
				+ "1. Display the transactions made by customers living in a given zipcode for a given Month and year. \n"
				+ "2. Display the number and total values of transactions for a given type. \n"
				+ "3. Display the number and total values of transactions for branches in a given state. \n\n"
				+ "Customer Detail: \n" 
				+ "4. Check the existing account details of a customer. \n"
				+ "5. Modify the existing account details of a customer. \n"
				+ "6. Generate monthly bill for a credit card number for a given month and year. \n"
				+ "7. Display the transactions made by a customer between two dates. \n" 
				+ "8. Exit \n" + "";
		
		while (!exit) {
			menu = InputValidation.getValidInteger(1, 8, "selection", selection, input);
			
			switch (menu) {
			case 1:
				TransactionRunner Transaction1 = new TransactionRunner();
				Transaction1.method1();
				InputValidation.pressEnter(input);
				break;
			case 2:
				TransactionRunner Transaction2 = new TransactionRunner();
				Transaction2.method2();
				InputValidation.pressEnter(input);
				break;
			case 3:
				TransactionRunner Transaction3 = new TransactionRunner();
				Transaction3.method3();
				InputValidation.pressEnter(input);
				break;
			case 4:
				CustomerRunner Customer1 = new CustomerRunner();
				Customer1.method1();
				InputValidation.pressEnter(input);
				break;
			case 5:
				CustomerRunner Customer2 = new CustomerRunner();
				Customer2.method2();
				InputValidation.pressEnter(input);
				break;
			case 6:
				CustomerRunner Customer3 = new CustomerRunner();
				Customer3.method3();
				InputValidation.pressEnter(input);
				break;
			case 7:
				CustomerRunner Customer4 = new CustomerRunner();
				Customer4.method4();
				InputValidation.pressEnter(input);
				break;
			case 8:
				System.out.println ("Thank you and goodbye!!");
				exit = true;
				break;
			default:
				System.out.println("It is not a correct #");
			}
		}
	}

}
