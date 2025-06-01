import { View, TextInput, TouchableOpacity, Text, StyleSheet } from "react-native";
import Button from "./Button";

interface LoginFormProps {
  email: string;
  password: string;
  onEmailChange: (text: string) => void;
  onPasswordChange: (text: string) => void;
  onLogin: () => void;
  onForgotPassword: () => void;
}

export default function LoginForm({
  email,
  password,
  onEmailChange,
  onPasswordChange,
  onLogin,
  onForgotPassword,
}: LoginFormProps) {
  return (
    <View style={styles.form}>
		<Text style={styles.label}>Email Address</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your email address"
        autoCapitalize="none"
        keyboardType="email-address"
        value={email}
        onChangeText={onEmailChange}
        placeholderTextColor="#C4C4C4"
      />
		<Text style={styles.label}>Password</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter your password"
        secureTextEntry
        value={password}
        onChangeText={onPasswordChange}
        placeholderTextColor="#C4C4C4"
      />
		<TouchableOpacity onPress={onForgotPassword} style={{width: "100%"}}>
		  <Text style={styles.forgotPassword}>Forgot Password?</Text>
		</TouchableOpacity>
      <Button onPress={onLogin} title="Login" />
    </View>
  );
}

const styles = StyleSheet.create({
	form: {
		width: "100%",
		alignItems: "center",
		marginTop: 30,
	},
	label: {
		width: "100%",
		fontSize: 14,
		color: "#000000",
		marginBottom: 8,
		textAlign: "left",
		fontWeight: 600,
	},
	input: {
		width: "100%",
		height: 49,
		borderColor: "#C4C4C4",
		borderWidth: 1,
		borderRadius: 8,
		paddingHorizontal: 15,
		marginBottom: 14,
		backgroundColor: "#fff",
		fontSize: 14,
		color: "#C4C4C4",
	},
  forgotPassword: {
		color: "#757575", 
		marginBottom: 10,
		textAlign: "right",
		fontSize: 14,
  },
});