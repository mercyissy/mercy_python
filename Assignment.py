def data_plan_options():
    Code = '*312#'
    inp_user = input('Code: ')
    if inp_user == Code:
        print(
            '''
            option;
            1. My Offer
            2. Data Plans
            3. N5000/18GB
            4. N3000/10GB
            5. N1500/5GB
            6. N500/2GB
            7. SMART DATA PLANS
            8. BORROW AIRTIME/DATA
            9. Family Plan
            * Next
            '''
        )
        option = input('option: ')
        if option == '1':
            print(
                '''
                option;
                1. N3000/10GB/30 days
                2. N4000/15GB/30 days 
                3. MORE DATA OFFER
                4. VOICE OFFER
                5. RECHARGE OFFER
                22. Back
                0. Menu
                '''
            )
            option = input('option: ')
            if option == '1':
                print(
                    """
                    option;
                    10GB for 30 days at N3000. After your plan finishes?
                    1. Continue browsing from airtime
                    2. stop my data
                    22. Back   
                    """)

            else:
                print('Invalid option! try again')     

        elif option == '2':
            print(
                '''
                option;
                1. Daily/Weekly Bundles
                2. Weekly Bundles
                3. Monthly Bundles
                4. More Data (Data++)
                5. Mega BUNDLES
                6. Big Data Plans
                *. Next
                22. Back
                0. Menu
                '''
            )

        elif option == '3':
            print(
                '''
                option;
                18GB for 30 days at N5000. After your plan finishes?
                1. Continue browsing from airtime
                2. stop my data
                22. Back
                '''
            )

        elif option == '4': 
            print(
                '''
                option;
                10GB for 30 days at N3000. After your plan finishes?
                1. Continue browsing from airtime
                2. stop my data
                22. Back
                '''
            )
        elif option == '5': 
            print(
                '''
                option;
                5GB for 30 days at N1500. After your plan finishes?
                1. Continue browsing from airtime
                2. stop my data
                22. Back
                '''
            )
        elif option == '6': 
            print(
                '''
                option;
                Bingo_500 has been successfully activated. /n Would you like to auto-renew at expiry
                1. Yes
                2. No - Do not auto-renew Reply
                22. Back
                0. Menu
                '''
            )

        elif option == '7':
            print(
                '''
                option;
                1. N400/1.5GB
                2. N800/3.5GB
                3. N600/1GB
                4. N1000/1.5GB
                5. N2000/7GB
                6. N5000/25GB
                7. N6000/23GB
                22. Back
                0. Menu
                '''
            )

        elif option == '8':
            print(
                '''
                option;
                0. Borrow Talk Time/Voice Bundle
                1. Eligibility and Help
                2. Borrow Credit
                3. Borrow Data
                4. Repay Loan
                5. Suspend Loan   
                *. Next
                '''
            )

        elif option == '9':
            print(
                '''
                option;
                1. Family Plan+
                2. Family Data Plan
                3. Booster Plan
                4. Manage Group
                22. Back
                0. Menu
                '''
            )

        elif option == '*':
            print(
                '''
                option;
                10. Everyday ON
                11. Super Binge
                12. Social Bundle
                13. Hourly Plan
                14. Gifting and Sharing
                15. Trybe Data Plan
                16. Data Balance
                0. Menu
                '''
            )

        else:
            print('Invalid option!')     

    else:
        print('invalid code. try again')
        exit()

data_plan_options()
