def lift_capacity_function(waiting_people, current_state_of_the_lift):
    for i in range(len(current_state_of_the_lift)):
        if waiting_people > 3:
            current_number_of_people = abs(4 - int(current_state_of_the_lift[i]))
            waiting_people -= current_number_of_people

            current_state_of_the_lift[i] += current_number_of_people
        else:
            current_waiting_people = abs(4 - int(current_state_of_the_lift[i]))
            if current_waiting_people > waiting_people:
                current_state_of_the_lift[i] += waiting_people
                waiting_people -= abs(waiting_people - current_waiting_people)

    if waiting_people > 0:
        print(f"There isn't enough space! {waiting_people} people in a queue!")
    elif sum(current_state_of_the_lift) != len(current_state_of_the_lift) * 4:
        print("The lift has empty spots!")

    return ' '.join([str(num) for num in current_state_of_the_lift])


number_of_people_waiting_to_get_on_the_lift = int(input())
lift_capacity = list(map(int, input().split()))
print(lift_capacity_function(number_of_people_waiting_to_get_on_the_lift, lift_capacity))