from django.shortcuts import render
from accounts.models import CustomUser
from .models import SearchEntry




def search_users(request):
    # Perform your search logic here, for example:
    query = request.GET.get('q', '')
    matching_users = CustomUser.objects.filter(username__icontains=query)

    # Create a search entry for the logged-in user
    if request.user.is_authenticated:
        # Fetch user details from the Users model
        user_details = CustomUser.objects.get(id=request.user.id)

        # Create a search entry and populate it with user details and the search query
        search_entry = SearchEntry.objects.create(
            user=request.user,
            query=query,
            age=user_details.age,
            iq_level=user_details.iq_level,
            coding_level=user_details.coding_level,
            address=user_details.address
        )

    return render(request, 'search_results_advanced.html', {'matching_users': matching_users})


