package runner;

import java.util.Scanner;
import dao.TransactionDaoImpl;
import java.sql.SQLException;

public class TransactionRunner {

	public void method1() throws SQLException {	
		int month, year;
		String zip;
		Scanner input = new Scanner(System.in);

		String selection1 = "\nPlease enter a valid Zip code. \n" + "";
		zip = InputValidation.getValidNumericString("Zip Code", selection1, 5, input);
		
		String selection2 = "\nPlease enter a valid Month as MM \n" + "";
		month = InputValidation.getValidInteger(1, 12, "Month", selection2, input);

		String selection3 = "\nPlease enter a valid year between "
				+ "1950 to 2018 as YYYY  \n" + "";
		year = InputValidation.getValidInteger(1950, 2018, "Year", selection3, input);
		
		TransactionDaoImpl TXDaoimpl1 = new TransactionDaoImpl();
		TXDaoimpl1.getbyZipcode(zip, month, year);
	} 

	public void method2() throws SQLException {
		String type;	
		Scanner input = new Scanner(System.in);
		String selection1 = "\nPlease select and enter the type from the list below. \n" + "" 
		                   + "\n'Education', 'Entertainment', 'Grocery', 'Gas', 'Bills', 'Test', 'Healthcare'\n ";
		type = InputValidation.getValidCategory("Type", selection1, input);
		TransactionDaoImpl TXDaoimpl2 = new TransactionDaoImpl();
		TXDaoimpl2.getbyType(type);
	}

	public void method3() throws SQLException {
		String state;
		Scanner input = new Scanner(System.in);
		String selection1 = "\nPlease enter a valid two character State code \n";
		state = InputValidation.getValidState("State", selection1, input);
		TransactionDaoImpl TXDaoimpl3 = new TransactionDaoImpl();
		TXDaoimpl3.getbyState(state);
	}
}