from django.test import TestCase
from django.contrib.auth.models import User
from UsersManager.models import Profile
from django.db.utils import IntegrityError

class ProfileModelTest(TestCase):
    """
    Teste unitare pentru modelul Profile
    """

    def setUp(self):
        # Creăm un user de bază pentru testare
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_create_profile_with_valid_data(self):
        """
        Verifică dacă putem crea un Profile valid
        """
        profile = Profile.objects.create(
            user=self.user,
            role="logistic_user_lvl1",
            id_number=12345
        )
        self.assertEqual(profile.user.username, "testuser")
        self.assertEqual(profile.role, "logistic_user_lvl1")
        self.assertEqual(profile.id_number, 12345)

    def test_role_choices_are_limited(self):
        """
        Verifică dacă rolul este unul dintre valorile permise (ROLE_CHOICE)
        """
        valid_roles = [choice[0] for choice in Profile.ROLE_CHOICE]
        profile = Profile.objects.create(
            user=self.user,
            role="logistic_manager",
            id_number=111
        )
        self.assertIn(profile.role, valid_roles)

    def test_one_to_one_relationship_unique_user(self):
        """
        Verifică dacă relația OneToOne nu permite 2 Profile pentru același User
        """
        Profile.objects.create(
            user=self.user,
            role="logistic_user_lvl1",
            id_number=222
        )
        with self.assertRaises(IntegrityError):
            Profile.objects.create(
                user=self.user,  # aceeași referință la user
                role="warehouse_manager",
                id_number=333
            )

    def test_id_number_accepts_integers_only(self):
        """
        Verifică dacă id_number este integer
        """
        profile = Profile.objects.create(
            user=self.user,
            role="warehouse_user_lvl1",
            id_number=999
        )
        self.assertIsInstance(profile.id_number, int)