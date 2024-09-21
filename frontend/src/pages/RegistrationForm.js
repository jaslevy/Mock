import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import RegisterFormBox from '../components/RegisterFormBox';

// See https://claritydev.net/blog/build-a-multistep-form-with-react-hook-form
const RegistrationForm = () => {
  const navigate = useNavigate();
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [step, setStep] = useState(1);

  const handleNextStep = () => {
    setStep(step + 1);
  };

  const handlePrevStep = () => {
    setStep(step - 1);
  };

  const onSubmit = (data) => {
    // Handle form submission, e.g., send data to backend API
    console.log(data);
    navigate('/login');
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
        <form onSubmit={handleSubmit(onSubmit)}>
          <label
            htmlFor="firstName"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            First Name:
          </label>
          <input
            type="text"
            id="firstName"
            {...register('firstName', { required: true })}
            className="border border-gray-300 rounded-lg p-2 w-full"
          />
          {errors.firstName && <p className="text-red-500">First name is required</p>}
          <label
            htmlFor="lastName"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            Last Name:
          </label>
          <input
            type="text"
            id="lastName"
            {...register('lastName', { required: true })}
            className="border border-gray-300 rounded-lg p-2 w-full"
          />
          {errors.lastName && <p className="text-red-500">Last name is required</p>}
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-full"
            type="submit"
          >
            Next
          </button>
        </form>
      )}
      {/* Add more form inputs for each step */}
    </RegisterFormBox>
  );
};

export default RegistrationForm;

