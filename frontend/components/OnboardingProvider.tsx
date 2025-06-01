import { StyleSheet, Image, View, Dimensions } from 'react-native'
import React, { ReactNode } from 'react'

const { height } = Dimensions.get('window')
const IMAGE_HEIGHT = height * 0.65

interface OnboardingProviderProps {
  children: ReactNode
}

const OnboardingProvider = ({ children }: OnboardingProviderProps) => {
  return (
    <View style={styles.container}>
      <Image
        source={require("../assets/images/onboarding-background.png")}
        style={styles.onboardingBackground}
        resizeMode="cover"
      />
      {children}
    </View>
  )
}

export default OnboardingProvider

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "flex-end",
  },
  onboardingBackground: {
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    height: IMAGE_HEIGHT,
    zIndex: 0,
  }
})