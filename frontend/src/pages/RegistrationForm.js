import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import RegisterFormBox from '../components/RegisterFormBox';

const RegistrationForm = () => {
  const navigate = useNavigate();
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({});

  const handleNextStep = () => {
    setStep(step + 1);
  };

  const handlePrevStep = () => {
    setStep(step - 1);
  };

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    setFormData((prevFormData) => {
      const interests = prevFormData.interests || [];
      if (checked) {
        interests.push(name);
      } else {
        interests.splice(interests.indexOf(name), 1);
      }
      return { ...prevFormData, interests };
    });
  };

  /// Outline but will need adjusting
  const onSubmit = async (data) => {
    try {
      const formData = new FormData();
      formData.append('username', data.username);
      formData.append('first_name', data.first_name);
      formData.append('last_name', data.last_name);
      formData.append('email', data.email);
      formData.append('bio', data.bio);
      // ... other form fields ...
  
      const response = await fetch('/users/', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        const userData = await response.json();
        console.log(userData);
        navigate('/MatchingInterface');
      } else {
        throw new Error('Failed to create user');
      }
    } catch (error) {
      console.error(error);
    }
  };

  const stepInputs = {
    1: (
      <>
        <label htmlFor="firstName" className="block text-gray-700 text-sm font-bold mb-2">
          First Name:
        </label>
        <input
          type="text"
          id="firstName"
          name="firstName"
          {...register('firstName', { required: true })}
          className="border border-gray-300 rounded-lg p-2 w-full"
          onChange={handleInputChange}
        />
        {errors.firstName && <p className="text-red-500">First name is required</p>}

        <label htmlFor="lastName" className="block text-gray-700 text-sm font-bold mb-2">
          Last Name:
        </label>
        <input
          type="text"
          id="lastName"
          name="lastName"
          {...register('lastName', { required: true })}
          className="border border-gray-300 rounded-lg p-2 w-full"
          onChange={handleInputChange}
        />
        {errors.lastName && <p className="text-red-500">Last name is required</p>}
      </>
    ),
    2: (
      <>
        <label className="block text-gray-700 text-sm font-bold mb-2">
          Why are you making an account?
        </label>
        <div className="flex gap-2">
          <input
            type="radio"
            id="seekingEmployment"
            name="accountReason"
            value="seekingEmployment"
            {...register('accountReason', { required: true })}
            onChange={handleInputChange}
          />
          <label htmlFor="seekingEmployment">Seeking Employment</label>
        </div>
        <div className="flex gap-2">
          <input
            type="radio"
            id="justPracticing"
            name="accountReason"
            value="justPracticing"
            {...register('accountReason', { required: true })}
            onChange={handleInputChange}
          />
          <label htmlFor="justPracticing">Just Practicing</label>
        </div>
      </>
    ),
    3: (
      <>
        <label className="block text-gray-700 text-sm font-bold mb-2">
          Interests:
        </label>
        <div className="flex flex-wrap gap-2">
          <input
            type="checkbox"
            id="mlAi"
            name="mlAi"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="mlAi">ML/AI</label>
          <input
            type="checkbox"
            id="dataEngineering"
            name="dataEngineering"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="dataEngineering">Data Engineering</label>
          <input
            type="checkbox"
            id="productEngineering"
            name="productEngineering"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="productEngineering">Product Engineering</label>
          <input
            type="checkbox"
            id="frontend"
            name="frontend"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="frontend">Frontend</label>
          <input
            type="checkbox"
            id="backend"
            name="backend"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="backend">Backend</label>
          <input
            type="checkbox"
            id="fullStack"
            name="fullStack"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="fullStack">FullStack</label>
          <input
            type="checkbox"
            id="uxUi"
            name="uxUi"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="uxUi">UX/UI</label>
          <input
            type="checkbox"
            id="ios"
            name="ios"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="ios">IOS</label>
          <input
            type="checkbox"
            id="android"
            name="android"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="android">Android</label>
          <input
            type="checkbox"
            id="devOps"
            name="devOps"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="devOps">DevOps</label>
          <input
            type="checkbox"
            id="securityEngineer"
            name="securityEngineer"
            onChange={handleCheckboxChange}
          />
          <label htmlFor="securityEngineer">Security Engineer</label>
        </div>
      </>
    ),
  };

  const stepTitles = {
    1: "What's your name?",
    2: 'Why are you making an account?',
    3: 'Interests',
  };
  return (
    <RegisterFormBox title={stepTitles[step]}>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="mb-4">{stepInputs[step]}</div>
        {step > 1 && (
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-full mb-4"
            type="button"
            onClick={handlePrevStep}
          >
            Back
          </button>
        )}
        {step !== Object.keys(stepInputs).length && (
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-full"
            type="button"
            onClick={handleNextStep}
          >
            Next
          </button>
        )}
        {step === Object.keys(stepInputs).length && (
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full w-full"
            type="submit"
          >
            Submit
          </button>
        )}
      </form>
    </RegisterFormBox>
  );
};

export default RegistrationForm;
