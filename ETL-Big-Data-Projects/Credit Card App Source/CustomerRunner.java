package runner;

import java.util.Scanner;
import dao.CustomerDaoImpl;
import java.sql.SQLException;

public class CustomerRunner {

	public void method1() throws SQLException {
		String ssn;
		
		String selection1 = "\nPlease enter a valid Social Security Number \n" + "";
		Scanner input = new Scanner(System.in);

		ssn = InputValidation.getValidNumericString("Number", selection1, 9, input);

		CustomerDaoImpl CustDaoimpl1 = new CustomerDaoImpl();
		CustDaoimpl1.CheckCustomer(ssn);
	}

	public void method2() throws SQLException {
		String CUST_ZIP, CUST_PHONE; 
		String FIRST_NAME, MIDDLE_NAME, LAST_NAME, APT_NO, STREET_NAME, CUST_CITY, CUST_STATE;
		String CUST_COUNTRY, CUST_EMAIL, SSN;
		int menu = 0;
		Scanner input = new Scanner(System.in);

		String selection1 = "\nPlease enter a valid Social Security Number to modify the record \n" + "";
		SSN = InputValidation.getValidNumericString("Number", selection1, 9, input);
		
		String selection = "\nSelect the number from the following menu you would like to modify. \n \n" 
				+ "1. Name Fields \n"
				+ "2. Address \n"
				+ "3. Phone \n"
				+ "4. Email \n"; 
				
		menu = InputValidation.getValidInteger(1, 4, "selection", selection, input);
		
		switch (menu) {
		case 1:
			FIRST_NAME = InputValidation.getValidName(40, "First Name", "Enter First Name (40 max characters):  ", input, true, true);
			MIDDLE_NAME = InputValidation.getValidName(40, "Middle Name", "Enter Middle Name (40 max characters):  ", input, true, true);
			LAST_NAME = InputValidation.getValidName(40, "Last Name", "Enter Last Name (40 max characters):  ", input, true, true);
					
			CustomerDaoImpl CustDaoimpl2a = new CustomerDaoImpl();
			CustDaoimpl2a.ModifyCustomerName(SSN, FIRST_NAME, MIDDLE_NAME, LAST_NAME);
		 	break; 
		case 2:
			APT_NO = InputValidation.getValidName(7, "Apartment number", "Enter Apartment number (7 max characters):  ", input, true, false);
			APT_NO = APT_NO.toUpperCase();	
			STREET_NAME = InputValidation.getValidName(30, "Street Name", "Enter Street Name (30 max characters):  ", input, true, false);			
			CUST_CITY = InputValidation.getValidName(30, "City", "Enter City (30 max characters):  ", input, true, true);			
			CUST_STATE = InputValidation.getValidState("State", "Enter State (2 character code):  ", input);
			CUST_ZIP = InputValidation.getValidNumericString("Zip Code", "Enter Zip (5 digit):  ", 5, input);
			CUST_COUNTRY = InputValidation.getValidName(30, "Country", "Enter Country (30 max characters):  ", input, true, true);

		 	CustomerDaoImpl CustDaoimpl2b = new CustomerDaoImpl();
		 	CustDaoimpl2b.ModifyCustomerAdd(SSN, APT_NO,STREET_NAME, CUST_CITY, CUST_STATE, CUST_COUNTRY, CUST_ZIP);
		 	break;
		case 3:
			CUST_PHONE = InputValidation.getValidNumericString("Phone Number", "Enter 7 digit Phone Number:  ", 7, input);
		 	CustomerDaoImpl CustDaoimpl2c = new CustomerDaoImpl();
		 	CustDaoimpl2c.ModifyCustomerPhone(SSN, CUST_PHONE);
		 	break;
		case 4:
			CUST_EMAIL = InputValidation.getValidEmail("Email", "Enter Email (40 characters max):  ", input);
			CustomerDaoImpl CustDaoimpl2d = new CustomerDaoImpl();
		 	CustDaoimpl2d.ModifyCustomerEmail(SSN, CUST_EMAIL);
		 	break;
		default:
			System.out.println("It is not a correct #");
		}	
	}
	
	public void method3() throws SQLException {
		String creditCard;
		int month, year;
		Scanner input = new Scanner(System.in);

		String selection1 = "\nPlease enter a valid Credit Card Number \n" + "";
		creditCard = InputValidation.getValidNumericString("Credit Card Number", selection1, 16, input);

		String selection2 = "\nPlease enter a valid Month as MM \n" + "";
		month = InputValidation.getValidInteger(1, 12, "Month", selection2, input);

		String selection3 = "\nPlease enter a valid year between " + "1950 to 2018 as YYYY  \n" + "";
		year = InputValidation.getValidInteger(1950, 2018, "Year", selection3, input);
		
		CustomerDaoImpl CustDaoimpl3 = new CustomerDaoImpl();
		CustDaoimpl3.GenerateBill(creditCard, month, year);
	}

	public void method4() throws SQLException {
		String ssn;
		int fromYear, toYear, fromMonth, toMonth, fromDay, toDay;
		Scanner input = new Scanner(System.in);

		String selection1 = "\nPlease enter a valid 9 digit Social Security Number \n" + "";
		ssn = InputValidation.getValidNumericString("Number", selection1, 9, input);

		String selection2 = "\nPlease enter a valid year between " + "1950 to 2018 as YYYY from  \n" + "";
		fromYear = InputValidation.getValidInteger(1950, 2018, "Year", selection2, input);

		String selection3 = "\nPlease enter a valid year between " + "1950 to 2018 as YYYY to \n" + "";
		toYear = InputValidation.getValidInteger(1950, 2018, "Year", selection3, input);

		String selection4 = "\nPlease enter a valid month as MM from \n" + "";
		fromMonth = InputValidation.getValidInteger(1, 12, "Month", selection4, input);

		String selection5 = "\nPlease enter a valid month as MM to \n" + "";
		toMonth = InputValidation.getValidInteger(1, 12, "Month", selection5, input);

		String selection6 = "\nPlease enter a valid day as DD from \n" + "";
		fromDay = InputValidation.getValidInteger(1, 31, "Day", selection6, input);

		String selection7 = "\nPlease enter a valid day as DD to \n" + "";
		toDay = InputValidation.getValidInteger(1, 31, "Day", selection7, input);

		if (toYear < fromYear || ((toYear == fromYear) && (toMonth < fromMonth))) {
			int tempYear = fromYear;
			int tempMonth = fromMonth;
			int tempDay = fromDay;
			fromYear = toYear;
			fromMonth = toMonth;
			fromDay = toDay;
			toYear = tempYear;
			toMonth = tempMonth;
			toDay = tempDay;
		}
		 
		CustomerDaoImpl CustDaoimpl4 = new CustomerDaoImpl();
		CustDaoimpl4.DisplayTrans(ssn, fromYear, toYear, fromMonth, toMonth, fromDay, toDay);
	}
}
