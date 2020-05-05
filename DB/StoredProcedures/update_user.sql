SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- ====================================================
-- Author:      Erick Andres Obregon Fonseca
-- Create date: 5th May 2020
-- Description: Update an user who matches with UserID
-- ====================================================

CREATE PROCEDURE updateUser
    @UserID int,
    @UserIDCard int,
    @UserName varchar(30),
    @UserLastName varchar(30),
    @UserPhoneNumber int,
    @UserEmail varchar(100)
AS

BEGIN
    SET NOCOUNT ON;

    UPDATE [user]
    SET [user].id_card = @UserIDCard,
        [user].[name] = @UserName,
        [user].last_name = @UserLastName,
        [user].phoneNumber = @UserPhoneNumber,
        [user].email = @UserEmail
    WHERE [user].id_user = @UserID;
END
GO
