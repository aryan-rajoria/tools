num_runs=1

command_to_run="python3 -m garak --model_type huggingface --model_name gpt2 --probes"

garak --list_probes > probes.txt
python replace.py "$command_to_run"

rm probes.txt

# this code assumes garak environment has been setup properly
# command to run gpt-2 on the garak model


# loop to create test directories
for (( i=0; i<num_runs; i++ ))
do
    test_dir="folder$i"
    mkdir -p "$test_dir"
    cp -f new.sh ./$test_dir/
    sudo chmod +x ./$test_dir/new.sh
    (cd "$test_dir" && ./new.sh)

    echo "Completed runs:$1"
done