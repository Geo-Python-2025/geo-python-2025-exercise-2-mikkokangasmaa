#!/usr/bin/env python3 

from points_decorator import points

class TestExercise2:
    #add points and feedback to the decorator
    @points(0.5,"Problem 1, Part 1: Something wrong with the `station_names` list!")
    #define test function
    def test_problem_1_part_1_names(self,ex2):
        #extract section data and namespace from the notebook
        section_data, namespace = ex2
        # Define the section key
        section = "Part 1"  
        #extract variables from the section data
        variables = section_data[section]['variables']
        #define station_name from the variables
        station_names = variables["station_names"]

        #start testing
        assert isinstance(station_names, list)
        assert len(station_names) == 5
        assert station_names == ["lighthouse", "Harmaja", "Suomenlinna aaltopoiju", "Kumpula", "Kaisaniemi"]
        


    @points(0.5,"Problem 1, Part 1: Something wrong with the `station_start_years` list!")
    def test_problem_1_part_1_years(self,ex2):
        section_data, namespace = ex2
        section = "Part 1"  # Define the section key
        variables = section_data[section]['variables']
        station_start_years = variables["station_start_years"]

        assert isinstance(station_start_years, list)
        assert len(station_start_years) == 5
        assert station_start_years == [2003, 1989, 2016, 2005, 1844]


    @points(0.5, "Problem 1, Part 2: Something wrong with ´station_names´ length or content!")
    def test_problem_1_part_2_station_names(self, ex2):
        section_data, namespace = ex2
        section = "Part 2"  # Define the section key
        variables = section_data[section]['variables']
        station_names = variables["station_names"]

        assert len(station_names) == 8, "station_names list length is incorrect!"
        assert station_names == ['lighthouse', 'Harmaja', 'Suomenlinna aaltopoiju', 'Kumpula', 'Kaisaniemi',
                                 'Malmi airfield', 'Vuosaari harbour', 'Kaivopuisto']

    @points(0.5, "Problem 1, Part 2: Something wrong with ´station_start_years´ length or content!")
    def test_problem_1_part_2_station_start_years(self, ex2):
        section_data, namespace = ex2
        section = "Part 2"  # Define the section key
        variables = section_data[section]['variables']
        station_start_years = variables["station_start_years"]

        assert len(station_start_years) == 8
        assert station_start_years == [2003, 1989, 2016, 2005, 1844, 1937, 2012, 1904]

    @points(0.5, "Problem 1, Part 3: Station names not found in section data or have incorrect values!")
    def test_problem_1_part_3_station_names(self, ex2):
        section_data, namespace = ex2
        section = "Part 3"  # Define the section key
        variables = section_data[section]['variables']
        station_names = variables["station_names"]

        assert station_names == ['Harmaja', 'Kaisaniemi', 'Kaivopuisto', 'Kumpula', 'Malmi airfield',
                                 'Suomenlinna aaltopoiju', 'Vuosaari harbour', 'lighthouse']
        

    @points(0.5, "Problem 1, Part 3: Station start years not found in section data or have incorrect values!")
    def test_problem_1_part_3_station_start_years(self, ex2):
        section_data, namespace = ex2
        section = "Part 3"  # Define the section key
        variables = section_data[section]['variables']
        station_start_years = variables["station_start_years"]

        assert station_start_years == [2016, 2012, 2005, 2003, 1989, 1937, 1904, 1844]

    @points(1, "Problem 2, Part 1: Something wrong with the months list!")
    def test_problem_2_part_1_months(self, ex2):
        section_data, namespace = ex2
        section = "Part 4"  # continue section tagging from problem 1
        variables = section_data[section]['variables']
        months = variables['months']

        assert months[3] == 'April'
        assert months[-1] == 'December'

    @points(2, "Problem 2, Part 1: Something wrong with the ´average_temp´ list!")
    def test_problem_2_part_1_average_temp(self, ex2):
        section_data, namespace = ex2
        section = "Part 4"  # continue section tagging from problem 1
        variables = section_data[section]['variables']
        average_temp = variables['average_temp']

        assert average_temp[3] == 4.0
        assert average_temp[-1] == -1.5

    
    @points(2, "Problem 2, Part 1: Variable `selected_month_index` is not integer type!")
    def test_problem_2_part_1_index(self, ex2):
        section_data, namespace = ex2
        section = "Part 4"  # continue section tagging from problem 1
        variables = section_data[section]['variables']

        assert isinstance(variables['selected_month_index'], int), "selected_month_index should be an integer!"
        

