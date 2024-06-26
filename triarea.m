function triarea(csv_files)
       % csv_files is expected to be a cell array of file paths

    n_files = numel(csv_files);
    all_data = cell(1, n_files);

    for ii = 1:n_files
        all_data{ii} = readtable(csv_files{ii});
    end

    % check the tables:
    disp('Previewing data from each file:');
    cellfun(@(x) disp(head(x)), all_data);

    % concatenate all the tables into one big table, and write it to output_file:
    output_file = 'combined_output.csv';  % You can modify this or pass it as an argument
    combined_table = cat(1, all_data{:});
    writetable(combined_table, output_file);

    % check that the resulting output file exists:
    disp('Files in current directory:');
    disp(dir('*.csv'));

    % check the contents of the resulting output file:
    disp('Preview of the combined output file:');
    disp(head(readtable(output_file)));
    
    disp(['Combined CSV file saved as: ' output_file]);
end