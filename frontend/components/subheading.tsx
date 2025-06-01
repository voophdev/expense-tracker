import { Text, StyleSheet } from 'react-native';

type SubHeadingProps = {
  subHeading: string;
};

export default function SubHeading({ subHeading }: SubHeadingProps) {
  return <Text style={styles.subHeading}>{subHeading}</Text>;
}

const styles = StyleSheet.create({
    subHeading: {
        fontSize: 20,
        fontWeight: 600,
        color: '#3E7C78',
        textAlign: 'center',
        fontFamily: 'Manrope'
    },
});