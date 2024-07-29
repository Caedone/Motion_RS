close all; 
clear;
clc;  
%****************************************************************************************************************************************************
% After running this you will still need to clean up the CSV file
% Open the "combined_output.csv" file using VScode
% Replace the labels (Line 1) with "Command,RegisterAddress,Timestamp,DataElement0"
% Utilize "find and replace all"and find the excess commas and replace with null (Done by leaving 'replace' bar blank)

% If you would like two choose 2 different values edit value1 and value2 to
% the desired cells

%****************************************************************************************************************************************************

% Define the file paths in order
csv_file_list = {
    'C:\Users\gangliagurdian\Desktop\Unsupervised Learning\Test_Data\Delte\MotionA1.csv',
    'C:\Users\gangliagurdian\Desktop\Unsupervised Learning\Test_Data\Delte\MotionB2.csv'
};

    n_files = numel(csv_file_list);
    all_data = cell(1, n_files);

    % Read the first file to get the 3rd column
    first_table = readtable(csv_file_list{1}, 'PreserveVariableNames', true);
    third_column = first_table{:, 3};
    rows_to_write = third_column;

    % Calculate subtraction
    value1 = str2double(third_column{end-1});
    value2 = str2double(third_column{end});
    subtraction = value2 - value1;
    sprintf('%.6f',subtraction);

    % Read and combine all files
    for ii = 1:n_files
        temp_table = readtable(csv_file_list{ii}, 'PreserveVariableNames', true);
        all_data{ii} = temp_table;
    end

    % Concatenate all the tables into one big table
    combined_table = vertcat(all_data{:});

    % Get the total number of rows
    total_rows = height(combined_table);
       
    % Initialize w
    w = true;

new_third_column = rows_to_write;
% Loop to generate new values for the 3rd column
for i = (length(rows_to_write) + 1):total_rows
    if w
        value3 = str2double(new_third_column{end}); % Use {} to get the content of the cell
        new_value = value3 + subtraction;
        new_third_column{i} = sprintf('%.6f', new_value); % Use sprintf to format the value to 6 decimal places
        w = false;
    else 
        value3 = new_value;
        new_value = value3 + subtraction;
        new_third_column{i} = sprintf('%.6f', new_value); % Use sprintf to format the value to 6 decimal places
    end
end

    % Replace the 3rd column in the combined table
    combined_table{:, 3} = new_third_column;

    % Write the combined table to output file
    output_file = 'combined_output.csv';
    writetable(combined_table, output_file, 'WriteVariableNames', true);

    % Display some information
    disp(['Combined CSV file saved as: ' output_file]);
    disp(['Number of rows in combined file: ' num2str(total_rows)]);
    disp(['Subtraction value used: ' num2str(subtraction)]);

    % Preview the contents of the resulting output file
    disp('Preview of the combined output file:');
    disp(head(combined_table));