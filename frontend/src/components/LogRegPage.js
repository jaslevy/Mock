import FooterBar from "./FooterBar";
import LogoBlack from "../assets/images/LogoBlack.png";
const LogRegPage = ({title, subtitle, children}) => {
  return (
    <html lang="en" className="h-screen">
      <head></head>
      <body className="h-screen flex flex-col items-center justify-center">
        <div className="absolute top-0 left-1/2 transform -translate-x-1/2 mt-5">
        <a href="/">
          <img src={LogoBlack} className="h-18 w-auto" alt="MockMe logo" />
         </a>
        </div>
        <a href="/" className="absolute top-0 left-0 flex items-center p-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-6 w-6 mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M15 19l-7-7 7-7"
            />
          </svg>
          <span className="text-2xl font-bold">Back</span>
        </a>
        <div className="bg-white p-12 rounded-lg shadow-md w-full max-w-3xl mx-auto">
          <div className="mt-12 text-center">
            <h1 className="text-6xl font-bold">{title}</h1>
            <p className="text-3xl mt-6">{subtitle}</p>
          </div>
          <div className="flex items-center justify-center mt-12">
            {children}
          </div>
        </div>
      </body>
      <FooterBar />
    </html>
  );
}

export default LogRegPage;
