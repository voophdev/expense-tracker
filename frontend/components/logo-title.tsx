import { Text, StyleSheet } from 'react-native';

type LogoTitleProps = {
  title: string;
};

export default function LogoTitle({ title }: LogoTitleProps) {
  return <Text style={styles.logoTitle}>{title}</Text>;
}

const styles = StyleSheet.create({
    logoTitle: {
        fontSize: 50,
        fontWeight: 700,
        color: '#3E7C78',
        textAlign: 'center',
        letterSpacing: -0.4,
        fontFamily: 'Inter'
    },
});