import { View, StyleSheet, Text, TouchableOpacity } from 'react-native'

export default function LoginPrompt({ onLogin }: { onLogin: () => void }) {
  return (
    <View style={styles.loginPromptRow}>
      <Text style={styles.loginPromptText}>Already have an account? </Text>
      <TouchableOpacity onPress={onLogin}>
        <Text style={styles.loginPromptLink}>Log in</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
    loginPromptRow: {
        flexDirection: "row",
        marginTop: 20,
        alignItems: "center",
        justifyContent: "center",
    },
        loginPromptText: {
        fontFamily: "Inter",
        fontSize: 14,
        color: "#444444",
    },
        loginPromptLink: {
        fontFamily: "Inter",
        fontSize: 14,
        color: "#438883",
        fontWeight: "bold",
    },
})
