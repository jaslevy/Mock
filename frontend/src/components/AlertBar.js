const AlertBar = () => {
  return (
    <div className="bg-red-500 text-white flex items-center justify-center py-2 px-4 sm:px-6 md:px-8">
      <p className="hidden sm:block text-center sm:text-left mr-2">
        MockMe beta has launched at Cornell Tech. Log in with your Cornell email and try it yourself!
      </p>
      <button className="bg-transparent border border-white text-white font-bold px-4 py-1 rounded-md">
        Demo
      </button>
    </div>
  );
};

export default AlertBar;

