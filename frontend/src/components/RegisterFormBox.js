import React from 'react';

const RegisterFormBox = ({ children, title }) => {
  return (
    <div className="flex items-center justify-center h-screen">
      <div className="bg-white rounded-lg shadow-lg p-8 w-1/2">
        <h2 className="text-2xl font-bold mb-4 text-center">{title}</h2>
        {children}
      </div>
    </div>
  );
};

export default RegisterFormBox;