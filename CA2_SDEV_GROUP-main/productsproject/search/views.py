from django.shortcuts import render
from accounts.models import CustomUser
from .models import SearchEntry



def search_users(request):
    group_contains = request.GET.get('group_contains', '')
    age_contains = request.GET.get('age_contains', '')
    username_contains = request.GET.get('username_contains', '')

    # Filtering users based on search parameters
    matching_users = CustomUser.objects.filter(
        group__name=group_contains,
        age=age_contains,
        username__icontains=username_contains
    )

    # Creating a search entry for the logged-in user
    if request.user.is_superuser:
        # Fetch user details from the Users model
        user_details = CustomUser.objects.get(id=request.user.id)

        # Creating a search entry and populating it with user details and the search query
        search_entry = SearchEntry.objects.create(
            user=request.user,
            query=f"{group_contains} {age_contains} {username_contains}",
            age=user_details.age,
            iq_level=user_details.iq_level,
            coding_level=user_details.coding_level,
            address=user_details.address,
            image=user_details.image


        )

    return render(request, 'search_results_advanced.html', {'matching_users': matching_users})