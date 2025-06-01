import { TouchableOpacity, Text, StyleSheet } from "react-native";

interface ButtonProps {
  onPress: () => void;
  title: string;
}

export default function Button({ onPress, title }: ButtonProps) {
  return (
    <TouchableOpacity
      onPress={onPress}
      style={styles.button}
    >
      <Text style={styles.loginButtonText}>{title}</Text>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
    button: {
        width: "100%",
        height: 48,
        backgroundColor: "#3E7C78",
        borderRadius: 25,
        alignItems: "center",
        justifyContent: "center",
        marginTop: 10,
        marginBottom: 10,
    },
    loginButtonText: {
        color: "#fff",
        fontSize: 14,
        fontWeight: 600,
    }
});