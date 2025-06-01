import { StyleSheet, Text, Image, View, TouchableOpacity } from 'react-native'
import { useRouter } from "expo-router";
import OnboardingProvider from '@/components/OnboardingProvider'
import LoginPrompt from '@/components/LoginPrompt';

export default function OnboardingScreen() {
    const router = useRouter();

    return (
        <OnboardingProvider>
            <Image 
              source={require("../assets/images/onboarding.png")} 
              style={styles.onboardingImage}
            />
            <Image 
              source={require("../assets/images/coint.png")} 
              style={styles.cointImage}
            />
            <Image 
              source={require("../assets/images/Donut.png")} 
              style={styles.donutImage}
            />
            <View style={styles.actionsContainer}>
              <Text style={styles.heading}>Spend Smarter</Text>
              <Text style={styles.heading}>Save More</Text>
              <TouchableOpacity style={styles.getStartedButton} onPress={() => router.replace("/")}>
                <Text style={styles.getStartedButtonText}>Get Started</Text>
              </TouchableOpacity>
            <View>
              <TouchableOpacity onPress={() => router.replace({ pathname: "/login"})}>
                <LoginPrompt onLogin={() => router.replace({ pathname: "/login" })} />
              </TouchableOpacity>
            </View>
          </View>
        </OnboardingProvider>
    )
}

const styles = StyleSheet.create({
  onboardingImage: {
    zIndex: 1,
    position: "absolute",
    resizeMode: "contain",
    width: "100%",
    height: "85%",
    top: -20
  },
  cointImage: {
    zIndex: 1,
    position: "absolute",
    resizeMode: "contain",
    width: "24%",
    height: "24%",
    top: 60,
    left: "13%",
  },
  donutImage: {
    zIndex: 1,
    position: "absolute",
    resizeMode: "contain",
    width: "20%",
    height: "20%",
    top: 122,
    right: "15%",
  },
  actionsContainer: {
    zIndex: 1,
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    top: 250,
  },
  heading: {
    fontFamily: 'Inter',
    fontSize: 36,
    fontWeight: 700,
    textAlign: "center",
    color: "#438883",
    lineHeight: 38,
    letterSpacing: -0.2,
  },
  getStartedButton: {
    marginTop: 20,
    alignItems: "center",
    justifyContent: "center",
    width: "90%",
    paddingHorizontal: 20,
    borderRadius: 40,
    paddingTop: 10,
    paddingBottom: 10,
    paddingLeft: 20,
    paddingRight: 20,
    backgroundColor: "#438883",
    elevation: 10,
  },
  getStartedButtonText: {
    fontFamily: "Inter",
    fontWeight: 700,
    fontSize: 18,
    lineHeight: 38,
    letterSpacing: -0.2,
    color: "#FFFFFF",
  },
});