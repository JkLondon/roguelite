def create_sprite(list,timer):
    return {'sprite':list,'timer':timer,'num':len(list)}

list_mob_stand = []
list_mob_stand.append('test_mob_stand(1).png')
list_mob_stand.append('test_mob_stand(2).png')
list_mob_go_left = []
list_mob_go_left.append('test_mob_go_right(1).png')
list_mob_go_left.append('test_mob_go_right(2).png')
list_mob_go_right = []
list_mob_go_right.append('test_mob_go_left(1).png')
list_mob_go_right.append('test_mob_go_left(2).png')

stand = create_sprite(list_mob_stand,timer=15)
go_left = create_sprite(list_mob_go_left,timer=1)
go_right = create_sprite(list_mob_go_right,timer=1)

TEST_MOB = {'stand': stand, 'go_left': go_left, 'go_right': go_right}

list_creature_stand = []
list_creature_stand.append('test_creature(1).png')
list_creature_stand.append('test_creature(2).png')

stand = create_sprite(list_creature_stand,timer=10)

TEST_CREATURE = {'stand':stand}
