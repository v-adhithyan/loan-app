"use client";
import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


const Home = () => {
  const [uuid, setUuid] = useState<string | null>(null);
  const [formData, setFormData] = useState({
    businessName: '',
    establishedYear: '',
    loanAmount: '',
    accountingProvider: '',
  });
  const [balanceSheet, setBalanceSheet] = useState<any[]>([]);
  const [submitMessage, setSubmitMessage] = useState<string | null>(null);
  const [showSubmitButton, setShowSubmitButton] = useState<boolean>(false);
  const [errorMessages, setErrorMessages] = useState<string[]>([]);

  const handleStartApplication = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/loan-application/initiate/', {
        method: 'POST',
      });
      const data = await response.json();
      setUuid(data.uuid);
      setShowSubmitButton(true); // Show the "Submit Application" button
      setSubmitMessage(null); // Clear the submit message
    } catch (error) {
      console.error('Error initiating loan application:', error);
    }
  };

  const handleAccountingProviderChange = async (provider: string) => {
    try {
      const response = await fetch(`http://localhost:8000/api/integration/${provider}/balance-sheet/`);
      const data = await response.json();
      setBalanceSheet(data);
    } catch (error) {
      console.error('Error fetching balance sheet:', error);
    }
  };

  const handleSubmitApplication = async () => {
    try {
      const data = {
        uuid: uuid,
        business_name: formData.businessName,
        established_year: formData.establishedYear,
        loan_amount: formData.loanAmount,
        accounting_provider: formData.accountingProvider,
        balance_sheet: balanceSheet,
      };
      const response = await fetch('http://localhost:8000/api/loan-application/submit/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (response.status === 201) {
        const data = await response.json();
        setSubmitMessage(data.message);
        // Clear all data except the UUID
        setFormData({
          businessName: '',
          establishedYear: '',
          loanAmount: '',
          accountingProvider: '',
        });
        setBalanceSheet([]);
        setShowSubmitButton(false); // Hide the "Submit Application" button
      } else if (response.status === 400) {
        const errorData = await response.json();
        const errorMessages = Object.values(errorData).flat(); // Extract and flatten error messages
        setErrorMessages(errorMessages); 
      }
      else {
        console.error('Application submission failed with status:', response.status);
        setSubmitMessage('Application submission failed. Please try again.');
      }
    } catch (error) {
      console.error('Error submitting loan application:', error);
      setSubmitMessage('An error occurred while submitting the application. Please try again later.');
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center">Loan Application</h1>
      {uuid === null ? (
        <button className="btn btn-primary" onClick={handleStartApplication}>
          Start Application
        </button>
      ) : (
        showSubmitButton ? (
          <div>
            <form>
              {errorMessages.length > 0 && (
                <div className="alert alert-danger mt-3">
                  {errorMessages.join(', ')}
                </div>
              )}
              <div className="mb-3">
                <label htmlFor="businessName" className="form-label">
                  Business Name:
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="businessName"
                  value={formData.businessName}
                  onChange={(e) => setFormData({ ...formData, businessName: e.target.value })}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="establishedYear" className="form-label">
                  Established Year:
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="establishedYear"
                  value={formData.establishedYear}
                  onChange={(e) => setFormData({ ...formData, establishedYear: e.target.value })}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="loanAmount" className="form-label">
                  Required Loan Amount:
                </label>
                <input
                  type="number"
                  className="form-control"
                  id="loanAmount"
                  value={formData.loanAmount}
                  onChange={(e) => setFormData({ ...formData, loanAmount: e.target.value })}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="accountingProvider" className="form-label">
                  Accounting Provider:
                </label>
                <select
                  className="form-select"
                  id="accountingProvider"
                  value={formData.accountingProvider}
                  onChange={(e) => {
                    setFormData({ ...formData, accountingProvider: e.target.value });
                    handleAccountingProviderChange(e.target.value);
                  }}
                >
                  <option value="">Select an option</option>
                  <option value="myob">MYOB</option>
                  <option value="xero">Xero</option>
                </select>
              </div>
            </form>
            {balanceSheet.length > 0 && (
              <div>
                <h2>Balance Sheet</h2>
                <table className="table table-bordered">
                  <thead>
                    <tr>
                      <th>Year</th>
                      <th>Month</th>
                      <th>Profit or Loss</th>
                      <th>Assets Value</th>
                    </tr>
                  </thead>
                  <tbody>
                    {balanceSheet.map((entry, index) => (
                      <tr key={index}>
                        <td>{entry.year}</td>
                        <td>{entry.month}</td>
                        <td>{entry.profitOrLoss}</td>
                        <td>{entry.assetsValue}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
            <button className="btn btn-primary" onClick={handleSubmitApplication}>
              Submit Application
            </button>
          </div>
        ) : (
          <div className="alert" role="alert">
            {submitMessage}
          </div>
        )
      )}
    </div>
  );
};

export default Home;
