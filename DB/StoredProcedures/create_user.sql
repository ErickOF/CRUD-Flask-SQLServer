SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:      Erick Andres Obregon Fonseca
-- Create date: 5th May 2020
-- Description: Create new user
-- =============================================

CREATE PROCEDURE createNewUser
    @UserIDCard int,
    @UserName varchar(30),
    @UserLastName varchar(30),
    @UserPhoneNumber int,
    @UserEmail varchar(100)
AS

BEGIN
    SET NOCOUNT ON;

    INSERT INTO [user] (id_card, [name], last_name, phoneNumber, email)
    VALUES (@UserIDCard, @UserName, @UserLastName, @UserPhoneNumber, @UserEmail);
END
GO
