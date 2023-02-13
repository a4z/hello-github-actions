echo "steps:"
while read line; do
  echo "  - name: Step with $line"
  echo "    run: echo \"Running step with $line\""
done < steps.txt > steps.yml

cat steps.yml
