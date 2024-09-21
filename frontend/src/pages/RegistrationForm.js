import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import RegisterFormBox from '../components/RegisterFormBox';

const RegistrationForm = () => {
  const navigate = useNavigate();
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    // Add other fields as needed for the 8 steps
  });

  const handleNextStep = () => {
    setStep(step + 1);
  };

  const handlePrevStep = () => {
    setStep(step - 1);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission, e.g., send data to backend API
    console.log(formData);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const stepTitles = {
    1: "What's your name?",
    2: 'Step 2: Password',
    // Add more step titles as needed
  };

  return (
    <RegisterFormBox
      title={stepTitles[step]}
      backButtonText={step > 1 ? 'Back' : undefined}
      onBackButtonClick={handlePrevStep}
    >
      {step === 1 && (
        <>
          <label
            htmlFor="firstName"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            First Name:
          </label>
          <input
            type="text"
            id="firstName"
            name="firstName"
            value={formData.firstName}
            onChange={handleInputChange}
            className="border border-gray-300 rounded-lg p-2 w-full"
          />
          <label
            htmlFor="lastName"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            Last Name:
          </label>
          <input
            type="text"
            id="lastName"
            name="lastName"
            value={formData.lastName}
            onChange={handleInputChange}
            className="border border-gray-300 rounded-lg p-2 w-full"
          />
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-full"
            onClick={handleNextStep}
          >
            Next
          </button>
        </>
      )}
      {/* Add more form inputs for each step */}
    </RegisterFormBox>
  );
};

export default RegistrationForm;

