import 'package:flutter/material.dart';

class StyledText extends StatelessWidget {
  final String text; // Add a text parameter to accept the input
  
  const StyledText(this.text, {super.key});
  
  @override
  Widget build(BuildContext context) {
    return Text(
      text, // Use the passed text
      style: const TextStyle(
        color: Colors.white,
        fontSize: 28.0,
      ),
    );
  }
}
