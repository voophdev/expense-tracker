import { View, Text, Image, StyleSheet, TouchableOpacity } from "react-native";
import { useRouter } from "expo-router";
import OnboardingProvider from "@/components/OnboardingProvider";
import LogoTitle from "@/components/logo-title";
import SubHeading from "@/components/subheading";
import LoginForm from "@/components/LoginForm";

export default function LoginScreen() {

    const router = useRouter();

    return (
        <OnboardingProvider>
            <Image source={require("../assets/images/coint.png")} style={styles.cointImage} />
            <Image source={require("../assets/images/Donut.png")} style={styles.donutImage} />
            <View style={styles.container}>
                <LogoTitle title="finua" />
                <SubHeading subHeading="Sign in to your account" />
                <LoginForm
                    email=""
                    password=""
                    onEmailChange={() => {}}
                    onPasswordChange={() => {}}
                    onLogin={() => {}}
                    onForgotPassword={() => {}}
                />
                <TouchableOpacity style={{ flexDirection: "row", marginTop: 4 }}>
                    <Text style={styles.promptSignup}>{`Don't have an account? `}</Text>
                    <Text 
                        style={[styles.promptSignup, { color: "#3E7C78" }]}
                        onPress={() => router.replace({ pathname: "/signup"})}
                    >Create an account
                    </Text>
                </TouchableOpacity>
            </View>
        </OnboardingProvider>
    );
}

const styles = StyleSheet.create({
  cointImage: {
    zIndex: 1,
    position: "absolute",
    resizeMode: "contain",
    width: "24%",
    height: "24%",
    top: 40,
    left: "11%",
  },
  donutImage: {
    zIndex: 1,
    position: "absolute",
    resizeMode: "contain",
    width: "35%",
    height: "35%",
    top: -45,
    right: "5%",
  },
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 40,
  },
  promptSignup: {
    fontFamily: 'Manrope', 
    fontSize: 12,
    fontWeight: 400,
    color: "#757575"
  },
});