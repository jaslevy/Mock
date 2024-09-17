import LogRegPage from "../components/LogRegPage";
import { GoogleButton } from "../components/GoogleButton";
export default function Login() {
    return (
        <LogRegPage
            title="Sign In"
            subtitle="View your matches and schedule mocks"
        >
            <GoogleButton text="Sign in with Google" />
        </LogRegPage>
    );
} 
